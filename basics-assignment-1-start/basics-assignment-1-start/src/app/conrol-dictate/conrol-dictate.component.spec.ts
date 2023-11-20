import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConrolDictateComponent } from './conrol-dictate.component';

describe('ConrolDictateComponent', () => {
  let component: ConrolDictateComponent;
  let fixture: ComponentFixture<ConrolDictateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ConrolDictateComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ConrolDictateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
