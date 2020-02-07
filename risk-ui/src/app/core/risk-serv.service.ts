import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class RiskServService {

  is_admin: boolean = false;
  user: string = '';
  roomCode: string = '';
  pass: string = '';
  players: string[] = [];
  can_add: boolean = true;

  constructor() { }

  setCode(user: string, roomCode: string, pass: string, admin: boolean) {
    this.user = user;
    this.roomCode = roomCode;
    this.pass = pass;
    this.is_admin = admin;
    this.players.push(user);
  }
}
