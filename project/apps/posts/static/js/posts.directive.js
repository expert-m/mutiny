app.directive('postsDir', function () {
    return {
        restrict: 'AE',
        replace: true,
        templateUrl: '/static/html/posts.list.html',
        scope: {
            posts: '='
        },

        controller: function ($scope, $timeout) {
            $scope.offset = 0;
            $scope.count = 10;
            $scope.isMorePosts = $scope.posts.length == $scope.size;

            $scope.morePosts = function () {
                ui.progress.start();

                $scope.offset += $scope.count;

                apiPost.getList($scope.offset, $scope.count).then(function (data) {
                    if (data.length < $scope.size) {
                        if (data.length == 0)
                            ui.alert('Посты закончились :)', 'info');
                        $scope.isMorePosts = false;
                    }

                    $timeout(function () {
                        ui.progress.done();
                        $scope.posts = $scope.posts.concat(data);
                    });
                }).catch(function () {
                    ui.alert();
                });
            };
        }
    };
});