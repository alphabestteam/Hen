import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-book-details',
  templateUrl: './book-details.component.html',
  styleUrls: ['./book-details.component.scss']
})
export class BookDetailsComponent {
  constructor(private http:HttpClient,private route: ActivatedRoute) {}
  book:any
  sumReview: number = 0;

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      const bookId = +params.get('id')!;
      this.fetchBookDetails(bookId)
    });
  }

  fetchBookDetails(bookId: number): void {
    const url = `http://localhost:8000/book/${bookId}`;
    this.http.get<any>(url).subscribe(
      (response) => {
        this.book = response
        console.log('Book Details:', response);
      },
      (error) => {
        console.error('Error fetching book details:', error);
      }
    );
  }

  hasPriceField(book: any): boolean {
    return 'price' in book;
  }

  sumOfReviews(data: number): void {
    this.sumReview = data;
    console.log('Data from ReviewsComponent:', data);
  }
}
