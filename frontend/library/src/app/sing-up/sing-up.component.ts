import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sing-up',
  templateUrl: './sing-up.component.html',
  styleUrls: ['./sing-up.component.scss']
})
export class SingUpComponent {

  constructor(private http:HttpClient,private router: Router){}
  data: any = {
    id: 0,
    user_name: '',
    email: '',
    password: ''
  };
  onSubmit(){
    this.http.post("http://localhost:8000/users/", this.data).subscribe(
      (response: any) => {
        if (response && response['user_created']) {
          this.router.navigate(['/login']);
        } else {
          alert('Failed to create user. Please try again.');
        }
      },
      (error) => {
        console.error('POST request failed:', error);
        alert('Failed to create user. Please try again.');
      }
    );
  }
}
