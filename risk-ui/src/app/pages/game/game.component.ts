import { Component, OnInit } from '@angular/core';
import * as country_conv from '../../core/json/country_conv.json';
import { RiskServService } from 'src/app/core/risk-serv.service.js';
import { MapStatus } from 'src/app/core/classes/Map_Status.js';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {
  turn_num: number = 0;
  curr_player: string = 'Bob';
  a_country: string = 'N/A';
  d_country: string = 'N/A';
  s_country: string = 'US';

  map_status: MapStatus = null;

  riskService: RiskServService;

  constructor(riskService: RiskServService) { 
    this.riskService = riskService;
  }

  ngOnInit() {
    console.log((country_conv as any).default);
  }

  sel_state(state: any) {
    this.s_country = state;
  }

  clicked_state(state: any) {
    console.log(state);
    if(this.a_country == 'N/A') {
      this.a_country = state;
    } else {
      this.d_country = state;
    }
  }
}
