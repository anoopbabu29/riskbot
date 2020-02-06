import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { RiskServService } from 'src/app/core/risk-serv.service';

@Component({
  selector: 'app-game-info',
  templateUrl: './game-info.component.html',
  styleUrls: ['./game-info.component.scss']
})
export class GameInfoComponent implements OnInit {
  router: Router;
  riskService: RiskServService;

  constructor(router: Router, riskService: RiskServService) { 
    this.router = router;
    this.riskService = riskService;
  }

  ngOnInit() {
  }

  startGame(){
    this.router.navigate(['/game'])
  }

}
