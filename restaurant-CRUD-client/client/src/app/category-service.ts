import {Injectable} from '@angular/core';
import {Apollo} from 'apollo-angular';
import {HttpLink} from 'apollo-angular-link-http';
import {InMemoryCache} from 'apollo-cache-inmemory';
import gql from 'graphql-tag';

@Injectable()
export class CategoryService {

  constructor(private apollo: Apollo) {
  }

  getAllCategories() {
    const query = gql`query{allCategories {
                                      id,name,description
                                    }}`;
    return this.apollo.query({
      query: query,
      fetchPolicy: 'network-only'
    }).toPromise<any>().then(response => response.data.allCategories.map(
      cat => {
        return {id: cat.id, name: cat.name, description: cat.description, isEditing: false};
      }));
  }

  updateCategory(category) {

    const mutation = gql`mutation{ updateCategory(categoryId:${category.id},categoryData:{name:"${category.name}",description:"${category.description}"}) {
                                              ok,category {
                                                id,name,description
                                              }
                                            }
                                          }`;
    return this.apollo.mutate({mutation: mutation}).toPromise().then(
      response => {
        return {...response.data.updateCategory.category, isEditing: false};
      });
  }

  createCategory(name, description = '') {

    const mutation = gql`mutation{
                      createCategory(categoryData:{name:"${name}"}){
                        ok,category{
                          id,name,category {
                            id,name,description
                          }
                        }
                      }
                    }`;

    return this.apollo.mutate({mutation: mutation}).toPromise().then(response => response.data.createCategory.category);
  }

  deleteCategory(categoryId) {

    const mutation = gql`mutation{deleteCategory(categoryId:${categoryId}){
                                      deleted,categoryDeletedId
                                    }
                                  }`;
    return this.apollo.mutate({mutation: mutation}).toPromise().then(response => response.data.deleteCategory.categoryDeletedId);
  }

}
