import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-book-card',
  templateUrl: './book-card.component.html',
  styleUrls: ['./book-card.component.scss']
})
export class BookCardComponent {
  books: any[] = [];

  constructor(private http:HttpClient,private router: Router){}

  ngOnInit(): void {
    this.fetchBooks();
  }

  fetchBooks(): void {
    this.http.get<any[]>('http://localhost:8000/uploadBook').subscribe(
      (response) => {
        this.books = response;
      },
      (error) => {
        console.error('Error fetching books:', error);
      }
    );
  }

  navigateToBookDetails(bookId: number) {
    this.router.navigate(['/book-details', bookId]);
  }

}
