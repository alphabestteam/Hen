import { Component } from '@angular/core';

@Component({
  selector: 'app-conrol-dictate',
  templateUrl: './conrol-dictate.component.html',
  styleUrl: './conrol-dictate.component.css'
})
export class ConrolDictateComponent {
  selectedAlert: boolean = true;
  repeatCount: number = 1;

  changeAlerts() : void {
    this.selectedAlert = !this.selectedAlert;
  }

  getRepeatArray(): number[] {
    const repeatArray: number[] = Array.from({ length: this.repeatCount }, (_, i) => i + 1);
    console.log(repeatArray);
    return repeatArray;
  }
}
