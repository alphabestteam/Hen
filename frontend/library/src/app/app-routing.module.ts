import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LogPageComponent } from './log-page/log-page.component';
import { SingUpComponent } from './sing-up/sing-up.component';
import { HomeComponent } from './home/home.component';
import { BookDetailsComponent } from './book-details/book-details.component';

const routes: Routes = [
  { path: 'book-details/:id', component: BookDetailsComponent },
  { path: 'home', component: HomeComponent},
  { path: 'login', component: LogPageComponent },
  { path: 'signup', component: SingUpComponent },
  { path: '**', redirectTo: 'login', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
