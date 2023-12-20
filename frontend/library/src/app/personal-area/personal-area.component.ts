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
}
