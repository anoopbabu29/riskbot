import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-start-screen',
  templateUrl: './start-screen.component.html',
  styleUrls: ['./start-screen.component.scss']
})
export class StartScreenComponent implements OnInit {
  router: Router;

  constructor(router: Router) { 
    this.router = router;
  }

  ngOnInit() {
  }

  joinRoom(roomCode: string, pass: string) {
    console.log(roomCode)
    console.log(pass);
    this.router.navigate(['/info']);
  }

}
