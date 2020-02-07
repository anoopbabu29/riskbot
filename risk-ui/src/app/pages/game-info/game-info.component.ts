import { Component, OnInit, isDevMode } from '@angular/core';
import { Router } from '@angular/router';
import { RiskServService } from 'src/app/core/risk-serv.service';
import * as io from 'socket.io-client';

@Component({
  selector: 'app-game-info',
  templateUrl: './game-info.component.html',
  styleUrls: ['./game-info.component.scss']
})
export class GameInfoComponent implements OnInit {
  router: Router;
  riskService: RiskServService;
  socket: SocketIOClient.Socket;
  players: string[];
  is_admin: boolean = false;

  constructor(router: Router, riskService: RiskServService) { 
    this.router = router;
    this.riskService = riskService;
    let connectionOptions: SocketIOClient.ConnectOpts = {};
    connectionOptions.forceNew = true;
    connectionOptions.reconnectionAttempts = 10;
    connectionOptions.timeout = 10000;
    if(isDevMode)
      this.socket = io.connect(`http://${window.location.hostname}:5000`, connectionOptions);
    else
      this.socket = io.connect();
    
    this.players = this.riskService.players;
    this.is_admin = this.riskService.is_admin;
  }

  ngOnInit() {
    console.log(this.riskService);
    if(this.riskService.is_admin) {
      this.socket.on(`new_player_admin_${this.riskService.roomCode}${this.riskService.pass}`, (data: any) => {
        console.log(data);
        if(this.riskService.can_add) {
          this.riskService.players.push(data['name']);
        }
        this.socket.emit('check_room', {
          'roomCode': this.riskService.roomCode, 
          'pass': this.riskService.pass, 
          'has_started': this.riskService.can_add
        });

        if(this.riskService.players.length >= 4) {
          this.riskService.can_add = false;
        }

        console.log(this.riskService);
      });

      this.socket.on(`upd_pl_rm_admin_${this.riskService.roomCode}${this.riskService.pass}`, (data) => {
        this.socket.emit(`update_room`, {
          'roomCode': this.riskService.roomCode, 
          'pass': this.riskService.pass,
          'players': this.riskService.players
        })
      });

    } else {
      this.socket.on(`update_list_${this.riskService.roomCode}${this.riskService.pass}`, (data) => {
        console.log(data)
        this.riskService.players = data['players'];
        this.players = this.riskService.players;
        console.log(this.riskService);
      });
      this.socket.emit('req_playerInfo', {'roomCode': this.riskService.roomCode, 'pass': this.riskService.pass});
    }
  }

  startGame(){
    this.riskService.can_add = false;
    this.router.navigate(['/game'])
  }

}
