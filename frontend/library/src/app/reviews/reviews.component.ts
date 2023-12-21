import { Component ,Input, OnInit} from '@angular/core';
import { ReviewServieService} from '../review-servie.service'
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.scss']
})
export class ReviewsComponent implements OnInit {
  @Input() bookType: string = ''; 
  bookId:number = 0
  
  reviews: any[] = [];

  constructor(private reviewService: ReviewServieService,private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.bookId = +params.get('id')!;
    });
    this.reviewService.getBookReviews(this.bookId).then(
      (data: any) => {
        this.reviews = data;
      },
      (error: any) => {
        console.error('Error fetching reviews:', error);
      }
    );
  }
}


