import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { RiskServService } from 'src/app/core/risk-serv.service';

@Component({
  selector: 'app-start-screen',
  templateUrl: './start-screen.component.html',
  styleUrls: ['./start-screen.component.scss']
})
export class StartScreenComponent implements OnInit {
  router: Router;
  riskService: RiskServService;

  constructor(router: Router, riskService: RiskServService) { 
    this.router = router;
    this.riskService = riskService;
  }

  ngOnInit() {
  }

  joinRoom(roomCode: string, pass: string) {
    this.riskService.setCode(roomCode, pass);
    this.router.navigate(['/info']);
  }

}
