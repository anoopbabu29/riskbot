import { Component, OnInit, Input } from '@angular/core';
import { MapStatus } from '../../core/classes/Map_Status';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {
  @Input()
  map_status: MapStatus;

  countLeave(evt) {
    document.getElementById('hilite').setAttribute( 'd', 'm0 0' );
  }

  countOver(evt) {
    let outline = evt.target.getAttribute('d');
    document.getElementById('hilite').setAttribute( 'd', outline );
  }

  constructor() { }

  ngOnInit(){}

  ngAfterViewInit() {
    let countries = document.querySelectorAll('.country');
    for(let i = 0; i < countries.length; i++) {
      // <span matBadge = "4" matBadgeOverlap = "false">Mail</span>
      let country_pos: ClientRect = countries[i].getBoundingClientRect();
      console.log(countries[i]);
      console.log(country_pos);
      this.addBadge(country_pos)
      countries[i].addEventListener('mouseover', this.countOver);
    }
    
    document.querySelectorAll('.sea').forEach(sea => {
      sea.addEventListener('mouseover', this.countLeave);
    });
  }

  addBadge(pos: ClientRect) {
    let new_badge: HTMLElement = document.getElementsByClassName('badgeCopy')[0].cloneNode(true) as HTMLElement;
    let offset: number = document.documentElement.scrollTop || document.body.scrollTop;    ;
    new_badge.setAttribute('matBadge', '0');
    new_badge.style.zIndex = '10';
    new_badge.style.position = 'absolute';
    new_badge.style.display = 'inline';
    new_badge.style.top = (pos.top + pos.height/2 +  offset).toString() + 'px';
    new_badge.style.left = (pos.left + pos.width/2 - 15).toString() + 'px';
    document.querySelector('app-map').appendChild(new_badge);
    console.log(new_badge);
  }
}
