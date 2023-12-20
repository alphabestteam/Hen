import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LogPageComponent } from './log-page/log-page.component';
import { SingUpComponent } from './sing-up/sing-up.component';
import { HomeComponent } from './home/home.component';
import { BookDetailsComponent } from './book-details/book-details.component';
import { PersonalAreaComponent } from './personal-area/personal-area.component';
import { UploadBooksComponent } from './upload-books/upload-books.component';
import { UpdateBookComponent } from './update-book/update-book.component';


const routes: Routes = [
  { path: 'update-books/:id', component:UpdateBookComponent},
  { path: 'upload-books', component:UploadBooksComponent},
  { path: 'personal-area', component:PersonalAreaComponent},
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
