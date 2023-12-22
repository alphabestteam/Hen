import { Component ,Input, Output,OnInit,EventEmitter} from '@angular/core';
import { ReviewServieService} from '../review-servie.service'
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';

@Component({
  selector: 'app-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.scss']
})
export class ReviewsComponent implements OnInit {
  @Input() bookName: string = ''; 
  @Input() bookType: string = '';
  @Output() sumOfReview = new EventEmitter<number>()

  bookId:number = 0
  
  reviews: any[] = [];

  constructor(private reviewService: ReviewServieService,private route: ActivatedRoute,private router: Router) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.bookId = +params.get('id')!;
    });
    this.reviewService.getBookReviews(this.bookId).then(
      (data: any) => {
        this.reviews = data;
        this.sumOfReview.emit(this.reviews.length);
      },
      (error: any) => {
        console.error('Error fetching reviews:', error);
      }
    );
  }
  addReview(): void {
    this.router.navigate(['/post-review',this.bookId,this.bookType]);
  }
}

