import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  displayDetails: boolean = false;
  secretMessage: string = 'Secret Password = tuna';
  clickCounter: number = 0;
  buttonClicks: number[] = [];

  toggleDetails(): void {
    this.displayDetails = !this.displayDetails;
    this.clickCounter++;
    this.buttonClicks.push(this.clickCounter);
  }
}
