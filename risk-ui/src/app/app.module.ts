import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { 
  MatRippleModule,
  MatButtonModule,
  MatToolbarModule,
  MatIconModule,
  MatSidenavModule,
  MatListModule,
  MatGridListModule,
  MatTabsModule,
  MatTableModule,
  MatFormFieldModule,
  MatProgressBarModule,
  MatCardModule,
  MatDialogModule,
  MatInputModule,
  MatBadgeModule,
  MatDividerModule
} from '@angular/material';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { StartScreenComponent } from './pages/start-screen/start-screen.component';
import { GameInfoComponent } from './pages/game-info/game-info.component';
import { GameComponent } from './pages/game/game.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MapComponent } from './components/map/map.component';

@NgModule({
  declarations: [
    AppComponent,
    StartScreenComponent,
    GameInfoComponent,
    GameComponent,
    NavbarComponent,
    MapComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    // Material UI Import
    MatButtonModule, 
    MatToolbarModule,
    MatIconModule,
    MatSidenavModule,
    MatRippleModule,
    MatListModule,
    MatGridListModule,
    MatTabsModule,
    MatTableModule,
    MatFormFieldModule,
    MatProgressBarModule,
    MatCardModule,
    MatInputModule,
    MatBadgeModule,
    MatDialogModule,
    MatDividerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
