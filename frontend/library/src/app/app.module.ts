import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { HomeComponent } from './home/home.component';
import { WellcomePageComponent } from './wellcome-page/wellcome-page.component';
import { LogPageComponent } from './log-page/log-page.component';
import { SingUpComponent } from './sing-up/sing-up.component';
import { NavbarComponent } from './navbar/navbar.component';
import { BookCardComponent } from './book-card/book-card.component';
import { BookDetailsComponent } from './book-details/book-details.component';
import { PersonalAreaComponent } from './personal-area/personal-area.component';
import { UploadBooksComponent } from './upload-books/upload-books.component';
import { UpdateBookComponent } from './update-book/update-book.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    WellcomePageComponent,
    LogPageComponent,
    SingUpComponent,
    NavbarComponent,
    BookCardComponent,
    BookDetailsComponent,
    PersonalAreaComponent,
    UploadBooksComponent,
    UpdateBookComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule { }
