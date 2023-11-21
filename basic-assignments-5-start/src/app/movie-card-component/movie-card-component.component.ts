import { Component,Input } from '@angular/core';
import { Movie } from '../StarWarsMovie';

@Component({
  selector: 'app-movie-card',
  templateUrl: './movie-card-component.component.html',
  styleUrls: ['./movie-card-component.component.scss']
})
export class MovieCardComponentComponent {
  @Input() movie: Movie | undefined;
}
