import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent  implements OnInit{
  user_name:any =''
  constructor(private router: Router){}
  ngOnInit(): void {
    this.getName()
  }
  getName():void{
    this.user_name = sessionStorage.getItem('user_name');
  }

}
