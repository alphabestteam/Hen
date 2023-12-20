import { Component,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-users-cards',
  templateUrl: './users-cards.component.html',
  styleUrls: ['./users-cards.component.scss']
})
export class UsersCardsComponent implements OnInit{
  users: any[] = [];

  constructor(private http:HttpClient){}

  ngOnInit(): void {
    const isAdmin = sessionStorage.getItem('id_admin') === 'true';

    if (isAdmin) {
      console.log("hen yair")
      this.fetchBooks();
    }
  }

  fetchBooks(): void {
    const url = `http://localhost:8000/users/`
    this.http.get<any[]>(url).subscribe(
      (response:any) => {
        console.log(response.data)
        this.users = response
      },
      (error) => {
        console.error('Error fetching books:', error);
      }
    );
  }

  deleteUser(email:string,password:string):void{
    const url = `http://localhost:8000/users/${email}/${password}/`
    this.http.delete(url).subscribe(
      (response: any) => {
        if (response && response['user_deleted']) {
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

}
