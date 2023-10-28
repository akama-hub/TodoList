import { Component, OnInit } from '@angular/core';
import { PostService } from 'src/app/services/post.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit{
  posts: any;
  constructor(private postService:PostService) {  }
  
  ngOnInit(): void {
    this.ALLPost();
  }
  ALLPost() {
    this.postService.getAllPost().subscribe(
      posts => {
        this.posts = posts;
        console.log(this.posts);
      }
    )
  }
}
