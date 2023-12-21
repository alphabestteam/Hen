import { TestBed } from '@angular/core/testing';

import { ReviewServieService } from './review-servie.service';

describe('ReviewServieService', () => {
  let service: ReviewServieService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ReviewServieService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
