import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LogPageComponent } from './log-page/log-page.component';
import { SingUpComponent } from './sing-up/sing-up.component';
import { HomeComponent } from './home/home.component';
import { BookDetailsComponent } from './book-details/book-details.component';
import { PersonalAreaComponent } from './personal-area/personal-area.component';
import { UploadBooksComponent } from './upload-books/upload-books.component';
import { UpdateBookComponent } from './update-book/update-book.component';
import { PostReviewComponent } from './post-review/post-review.component';
import { authGuard } from './auth.guard';


const routes: Routes = [
  { path: 'post-review/:bookId/:bookType', component:PostReviewComponent, canActivate:[authGuard]},
  { path: 'update-books/:id', component:UpdateBookComponent, canActivate:[authGuard]},
  { path: 'upload-books', component:UploadBooksComponent, canActivate:[authGuard]},
  { path: 'personal-area', component:PersonalAreaComponent, canActivate:[authGuard]},
  { path: 'book-details/:id', component: BookDetailsComponent, canActivate:[authGuard] },
  { path: 'home', component: HomeComponent , canActivate:[authGuard]},
  { path: 'login', component: LogPageComponent },
  { path: 'signup', component: SingUpComponent },
  { path: '**', redirectTo: 'login', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
