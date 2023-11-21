import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AllMoviesComponent } from './all-movies/all-movies.component';
import { MovieCardComponentComponent } from './movie-card-component/movie-card-component.component';

@NgModule({
  declarations: [
    AppComponent,
    AllMoviesComponent,
    MovieCardComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
