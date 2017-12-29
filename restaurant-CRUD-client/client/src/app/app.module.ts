import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {ApolloModule} from 'apollo-angular';
import {HttpLinkModule} from 'apollo-angular-link-http'

import {AppComponent} from './app.component';
import {CategoryService} from './category-service';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {DishService} from './dish.service';

import {Apollo} from 'apollo-angular';
import {HttpLink} from 'apollo-angular-link-http';
import {InMemoryCache} from 'apollo-cache-inmemory'
@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ApolloModule,
    HttpLinkModule,
    FormsModule
  ],
  providers: [CategoryService, DishService],
  bootstrap: [AppComponent]
})
export class AppModule {

  constructor(private apollo: Apollo,
              private httpLink: HttpLink) {

    this.apollo.create({
      link: this.httpLink.create({uri: 'http://localhost:8000/graphql'}),
      cache: new InMemoryCache()
    });
  }


}
