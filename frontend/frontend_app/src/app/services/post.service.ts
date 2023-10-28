import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PostService {
  // DjangoサーバのURL
  api_link: string = "http://localhost:4000/";

  constructor(private http: HttpClient) { }

  getAllPost() {
    // Django レストサーバからすべてのPOSTを受け取る
    return this.http.get(this.api_link + `api/posts/`);
  }
}