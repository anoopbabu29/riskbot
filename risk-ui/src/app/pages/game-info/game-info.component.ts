import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-game-info',
  templateUrl: './game-info.component.html',
  styleUrls: ['./game-info.component.scss']
})
export class GameInfoComponent implements OnInit {
  router: Router;

  constructor(router: Router) { 
    this.router = router;
  }

  ngOnInit() {
  }

  startGame(){
    this.router.navigate(['/game'])
  }

}
