import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-personal-area',
  templateUrl: './personal-area.component.html',
  styleUrls: ['./personal-area.component.scss']
})
export class PersonalAreaComponent implements OnInit{
  borrowBooks: any[] = [];
  sellBooks: any[] = [];

  constructor(private http:HttpClient,private router: Router){}

  ngOnInit(): void {
    this.fetchBooks();
  }

  fetchBooks(): void {
    const id = sessionStorage.getItem('id')
    const url = `http://localhost:8000/userBooks/${id}`
    this.http.get<any[]>(url).subscribe(
      (response:any) => {
        this.borrowBooks = response['borrow_books']
        this.sellBooks = response['sell_books']
      },
      (error) => {
        console.error('Error fetching books:', error);
      }
    );
  }

  deleteBook(book_id:number):void{
    const url = `http://localhost:8000/deleteBook/${sessionStorage.getItem('id')}/${book_id}/`
    this.http.delete(url).subscribe(
      (response: any) => {
        if (response && response['book_deleted']) {
          this.fetchBooks();
        } else {
          alert('Failed to delete book. Please try again.');
        }
      },
      (error) => {
        console.error('DELETE request failed:', error);
        alert('Failed to delete book. Please try again.');
      }
    );
  }
  updateBook(bookId:number):void{
    this.router.navigate(['/update-books/',bookId])
  }
}
