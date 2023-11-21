import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MovieCardComponentComponent } from './movie-card-component.component';

describe('MovieCardComponentComponent', () => {
  let component: MovieCardComponentComponent;
  let fixture: ComponentFixture<MovieCardComponentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MovieCardComponentComponent]
    });
    fixture = TestBed.createComponent(MovieCardComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
