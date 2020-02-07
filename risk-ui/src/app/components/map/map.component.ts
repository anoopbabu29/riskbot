import { Component, OnInit, Input, HostListener, Output, EventEmitter } from '@angular/core';
import { MapStatus } from '../../core/classes/Map_Status';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {
  @Input()
  map_status: MapStatus;
  s_state_val: string = '';
  @Output()
  s_state = new EventEmitter();
  @Output()
  c_state = new EventEmitter();

  public onKeyDown = (event) => {
    console.log('hi');
    if(this.s_state_val != '') {
      this.c_state.emit(this.s_state_val);
    }
  }

  countLeave(evt) {
    document.getElementById('hilite').setAttribute('d', 'm0 0' );
  }

  private countOver = (evt) => {
    let outline = evt.target.getAttribute('d');
    this.s_state_val = evt.target.id.toString();
    document.getElementById('hilite').setAttribute( 'd', outline );
    console.log(this.s_state);
    this.s_state.emit(this.s_state_val);
  }

  private countClick = (evt) => {
    console.log(this.s_state_val);
    this.c_state.emit(this.s_state_val)
  }

  constructor() { }

  ngOnInit(){}

  @HostListener('window:resize', ['$event'])
  onResize(event) {
    this.refresh_map();
  }

  ngAfterViewInit() {
    this.refresh_map();
  }

  refresh_map() {
    document.querySelectorAll('.new_badges').forEach(badg => {
      badg.parentNode.removeChild(badg);
    });
    let countries = document.querySelectorAll('.country');
    for(let i = 0; i < countries.length; i++) {
      let country_pos: ClientRect = countries[i].getBoundingClientRect();
      console.log(countries[i]);
      console.log(country_pos);
      this.addBadge(country_pos);
      countries[i].addEventListener('mouseover', this.countOver);
    }

    document.getElementById('svg').addEventListener('click', this.countClick);
    
    document.querySelectorAll('.sea').forEach(sea => {
      sea.addEventListener('mouseover', this.countLeave);
    });
  }

  addBadge(pos: ClientRect) {
    let new_badge: HTMLElement = document.getElementsByClassName('badgeCopy')[0].cloneNode(true) as HTMLElement;
    let offset: number = document.documentElement.scrollTop || document.body.scrollTop;    ;
    new_badge.setAttribute('matBadge', '0');
    new_badge.setAttribute('matBadgeColor', 'gray');
    new_badge.style.zIndex = '10';
    new_badge.style.position = 'absolute';
    new_badge.style.display = 'inline';
    (new_badge.firstChild as HTMLElement).style.backgroundColor = 'gray';
    new_badge.style.top = (pos.top + pos.height/2 +  offset).toString() + 'px';
    new_badge.style.left = (pos.left + pos.width/2 - 15).toString() + 'px';
    new_badge.className += ' new_badges';
    document.querySelector('app-map').appendChild(new_badge);
    console.log(new_badge);
  }
}
