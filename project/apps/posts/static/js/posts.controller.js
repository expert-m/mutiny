var ListPostsCtrl = function ($scope, apiPost, $timeout, ui, posts) {
    $scope.posts = posts;
    window.console.log(posts);
};

ListPostsCtrl.resolve = {
    posts: function (api) {
        return api('posts').getPage(0, 10);
    }
};

app.controller('ListPostsCtrl', ListPostsCtrl);


var PostCtrl = function ($scope, $rootScope, $timeout, ui, $routeParams, post) {
    $scope.post = post;
    $rootScope.title = $scope.post.title;
};

PostCtrl.resolve = {
    post: function ($route, api) {
        return api('posts').getObject($route.current.params.id);
    }
};

app.controller('PostCtrl', PostCtrl);
