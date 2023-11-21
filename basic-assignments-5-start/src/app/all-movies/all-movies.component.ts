import { Component, OnInit } from '@angular/core';
import {Movie} from '../StarWarsMovie';
import { ActivatedRoute, Router } from '@angular/router';
import { FILMS } from '../star-wars-fake-db/film-data';


@Component({
  selector: 'app-all-movies',
  templateUrl: './all-movies.component.html',
  styleUrls: ['./all-movies.component.scss']
})
export class AllMoviesComponent implements OnInit{
  movies: Movie[]=[];
  
  constructor(private route: ActivatedRoute, private router: Router) {}

  ngOnInit(){
    this.movies = FILMS;
  }
}
