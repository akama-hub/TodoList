import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { PostComponent } from './post/post/post.component';
import { HttpClientModule } from '@angular/common/http';

const routes: Routes = [
  { path: '', component: PostComponent, pathMatch: 'full'},
  // { path: '/', component: PostComponent, pathMatch: 'full'}
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    HttpClientModule
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
