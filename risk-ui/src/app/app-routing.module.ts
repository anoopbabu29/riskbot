import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { StartScreenComponent } from './pages/start-screen/start-screen.component';
import { GameInfoComponent } from './pages/game-info/game-info.component';
import { GameComponent } from './pages/game/game.component';

const routes: Routes = [
  {path: '', redirectTo: 'start', pathMatch: 'full' },
  {path: 'start', component: StartScreenComponent},
  {path: 'info', component: GameInfoComponent},
  {path: 'game', component: GameComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
