import { Component, OnInit, isDevMode } from '@angular/core';
import { Router } from '@angular/router';
import { RiskServService } from 'src/app/core/risk-serv.service';
import * as io from 'socket.io-client';


@Component({
  selector: 'app-start-screen',
  templateUrl: './start-screen.component.html',
  styleUrls: ['./start-screen.component.scss']
})
export class StartScreenComponent implements OnInit {
  router: Router;
  riskService: RiskServService;
  socket: SocketIOClient.Socket;

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
  }

  ngOnInit() {
    this.socket.on('test_response', () => console.log('hi there'))
    this.socket.emit('test', null);

    
  }

  joinRoom(user: string, roomCode: string, pass: string, is_admin: boolean) {
    this.riskService.setCode(user, roomCode, pass, is_admin);
    if(is_admin){
      console.log('hi');
      console.log(this.riskService);
      this.socket.emit('create_room', {'roomCode': this.riskService.roomCode, 'pass': this.riskService.pass});
      this.router.navigate(['/info']);
    } else {
      console.log('h0');
      console.log(this.riskService);
      this.socket.on(`cpn_${this.riskService.roomCode}${this.riskService.pass}`, (data: any) => {
        console.log(data)
        if(data['can_join']) {
          this.router.navigate(['/info']);
        }  else {
          console.log('Cannot join room');
          this.socket.emit(`leave_room_${this.riskService.roomCode}${this.riskService.pass}`, {
            'roomCode': this.riskService.roomCode, 
            'pass': this.riskService.pass
          });
        }
      });
      console.log(`cpn_${this.riskService.roomCode}${this.riskService.pass}`);
      
      this.socket.emit('req_room', {
        'roomCode': this.riskService.roomCode, 
        'pass': this.riskService.pass,
        'name': user
      });
    }
  }
}
