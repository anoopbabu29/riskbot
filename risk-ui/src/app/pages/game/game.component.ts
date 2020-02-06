import { Component, OnInit } from '@angular/core';
import * as country_conv from '../../core/json/country_conv.json';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {

  turn_num: number = 0;
  curr_player: string = 'Bob';
  a_country: string = 'US';
  d_country: string = 'Russia';
  s_country: string = 'US';

  constructor() { }

  ngOnInit() {
    console.log((country_conv as any).default);
  }

}
