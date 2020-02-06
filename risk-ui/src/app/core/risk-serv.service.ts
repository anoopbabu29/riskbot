import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class RiskServService {

  roomCode: string = '';
  pass: string = '';

  constructor() { }

  setCode(roomCode: string, pass: string) {
    this.roomCode = roomCode;
    this.pass = pass;
  }
}
