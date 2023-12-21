import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ReviewServieService {

  private url = 'http://localhost:8000/review/'

  constructor(private http: HttpClient){}

  getReviews(): Promise<any[]> {
    return this.http.get<any[]>(this.url)
      .toPromise()
      .catch(this.handleError);
  }

  postReview(reviewData: any): Promise<any> {
    return this.http.post(this.url, reviewData)
      .toPromise()
      .catch(this.handleError);
  }

  getBookReviews(bookId: number): Promise<any[]> {
    return this.http.get<any[]>(`${this.url}${bookId}/`)
      .toPromise()
      .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }

}
