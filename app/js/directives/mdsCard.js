function MdsCard() {

    return {
        restrict: 'E',
        templateUrl: 'directives/mdsCard.html',
        scope: {
            song: '=',
            type: '@'
        },
        link: (scope, element) => {
            scope.typeProps = {
                'now-playing': {
                    flex: '66',
                    hr: 'Now Playing',
                    css: 'mds-card-now-playing'
                },
                'up-next': {
                    flex: '33',
                    hr: 'Up Next',
                    css: 'mds-card-up-next'
                },
                undefined: {
                    flex: '25',
                    css: 'mds-card-normal'
                }
            }[scope.type];
            element.addClass('layout-column');
            element.addClass('flex-' + scope.typeProps.flex);
            element.addClass(scope.typeProps.css);
        }
    };
}

export default {
    name: 'mdsCard',
    fn: MdsCard
};
