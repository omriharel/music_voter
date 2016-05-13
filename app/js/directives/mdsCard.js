function MdsCard() {

    return {
        restrict: 'E',
        templateUrl: 'directives/mdsCard.html',
        scope: {
            song: '=',
            type: '@'
        },
        link: (scope, element, attrs) => {
            element.addClass('layout-column');
            element.addClass('flex-' + (function () {
                switch (scope.type) {
                    case 'now-playing':
                        return '66';
                    case 'up-next':
                        return '33';
                    default:
                        return '25';
                }
            })());
        }
    };
}

export default {
    name: 'mdsCard',
    fn: MdsCard
};
