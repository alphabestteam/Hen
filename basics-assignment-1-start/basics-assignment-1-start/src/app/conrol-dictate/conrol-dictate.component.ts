import { Component } from '@angular/core';

@Component({
  selector: 'app-conrol-dictate',
  templateUrl: './conrol-dictate.component.html',
  styleUrl: './conrol-dictate.component.css'
})
export class ConrolDictateComponent {
  selectedAlert: boolean = true;
  repeatCount: number = 1;
  readonly repeatOptions: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  changeAlerts() : void {
    this.selectedAlert = !this.selectedAlert;
  }

  getRepeatArray(): number[] {
    const repeatArray: number[] = Array.from({ length: this.repeatCount }, (_, i) => i + 1);
    console.log(repeatArray);
    return repeatArray;
  }
}
