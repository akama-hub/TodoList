import { Component, OnInit } from '@angular/core';
import { PostService } from '../services/post.service';
import { ToDoList } from './todo_list';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {
  constructor(
    private postService: PostService
  ) { }

  posts: ToDoList[] = [];

  ngOnInit(): void {
    this.postService.getAllPost().subscribe(
      posts => {this.posts = posts}
    );
  }
}
