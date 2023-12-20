import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-upload-books',
  templateUrl: './upload-books.component.html',
  styleUrls: ['./upload-books.component.scss']
})
export class UploadBooksComponent {

  constructor(private http:HttpClient,private router: Router){}

  data: any = {
    owner_email: sessionStorage.getItem('email'),
    book_name: '',
    author_name: '',
    user: sessionStorage.getItem('id'),
    book_type: '',
    // price: 0,
  };
  onSubmit(){
    this.http.post("http://localhost:8000/uploadBook/", this.data).subscribe(
      (response: any) => {
        if (response && response['book_created']) {
          this.router.navigate(['/personal-area']);
        } else {
          alert('Failed to create book. Please try again.');
        }
      },
      (error) => {
        console.error('POST request failed:', error);
        alert('Failed to create book. Please try again.');
      }
    );
  }
}
