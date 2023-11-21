import { Component, EventEmitter, Input, Output  } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})
export class MyInnerComponent {
  @Input() initialInnerTotal: number = 0;
  innerTotal: number = 0;

  @Output() incrementOuterTotal = new EventEmitter<number>();
  @Output() decrementOuterTotal = new EventEmitter<number>();

  ngOnInit(): void {
    this.innerTotal = this.initialInnerTotal;
  }

  decreaseInnerTotal(): void {
    this.innerTotal--;
    if (this.innerTotal === -10) {
      this.decrementOuterTotal.emit(10);
      this.innerTotal = 0;
    }
  }

  increaseInnerTotal(): void {
    this.innerTotal++;
    if (this.innerTotal === 10) {
      this.incrementOuterTotal.emit(10);
      this.innerTotal = 0;
    }
  } 
}
