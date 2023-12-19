import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-log-page',
  templateUrl: './log-page.component.html',
  styleUrls: ['./log-page.component.scss']
})
export class LogPageComponent implements OnInit{
  constructor(private http:HttpClient,private router: Router){}
  data:any ={
    email:'',
    password:''
  };
  ngOnInit(): void {
    
  }
  onSubmit():void {
    const url = `http://localhost:8000/users/${this.data.email}/${this.data.password}`;
    this.http.get(url).subscribe(
      (response: any) => {
        if (response && response['user_exist']) {
          this.router.navigate(['/home']);
        } else {
          alert('Failed to connect. Please try again.');
        }
      },
      (error) => {
        console.error('Get request failed:', error);
        alert('Failed to connect. Please try again.');
      }
    );
  }
  goToSignUp(): void {
    this.router.navigate(['/signup']);
  }
}
