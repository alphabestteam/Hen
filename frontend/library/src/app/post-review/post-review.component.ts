import { Component,OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ReviewServieService } from '../review-servie.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-post-review',
  templateUrl: './post-review.component.html',
  styleUrls: ['./post-review.component.scss']
})
export class PostReviewComponent implements OnInit{
  review:any ={
    comment:'',
    user:sessionStorage.getItem('id'),
  };

  bookId: number = 0;
  bookType: string = '';

  constructor(private reviewService: ReviewServieService,
    private route: ActivatedRoute,private router: Router) {
      this.route.queryParams.subscribe(params => {
        this.bookId = +params['bookId'] || 0;
        this.bookType = params['bookType'] || '';
      });
    }
  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.bookId = +params.get('bookId')!;
      this.bookType = params.get('bookType')!;
    });
  }

    async postReview() {
      this.review.object_id = this.bookId;
      
      if (this.bookType.toLowerCase() === 'borrow') {   
        this.review.content_type = 2;
      } else if (this.bookType.toLowerCase() === 'sell') {
        this.review.content_type = 3;
      }

      try {
        const response = await this.reviewService.postReview(this.review);
        console.log('Review posted successfully', response);
      } catch (error) {
        console.error('Error posting review:', error);
      }

      this.router.navigate(['/home']);
    }
}
