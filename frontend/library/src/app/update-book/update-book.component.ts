import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-update-book',
  templateUrl: './update-book.component.html',
  styleUrls: ['./update-book.component.scss']
})
export class UpdateBookComponent {

  constructor(private http:HttpClient,private router: Router,private route: ActivatedRoute){}

  data: any = {
    owner_email: sessionStorage.getItem('email'),
    book_name: '',
    author_name: '',
    book_type: '',
    user: sessionStorage.getItem('id'),
    // price: 0,
  };
  bookId:number= 0

  onSubmit():void{
    this.route.paramMap.subscribe(params => {
      this.bookId = +params.get('id')!;
    });
    const url = `http://localhost:8000/book/${this.bookId}`
    this.http.put(url, this.data).subscribe(
      (response: any) => {
        if (response ) {
          this.router.navigate(['/personal-area']);
        } else {
          alert('Failed to update book. Please try again.');
        }
      },
      (error) => {
        console.error('PUT request failed:', error);
        alert('Failed to update book.');
      }
    );
  }
}
