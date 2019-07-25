marks = {
    "# ": [
        '''
          <button class="btn btn-primary" type="button" data-toggle="collapse"
        aria-expanded="false" data-target="#collapse1">
        ''',
        '''
          <span id="display1"> </span> </button>
          <div class="collapse" id="collapse1" onclick="calculate('collapse1',
        'display1', 'grade');">
          '''
    ],
    "--": ['''</div> ''', """ """
           ],
    "- [ ]": [
        '''<div class="checkbox">
          <label>
            <input type="checkbox" value="" id="1">
            <span class="cr"><i class="cr-icon glyphicon glyphicon-ok"></i></span>
        ''',
        '''
            </label>
         </div>
        '''
    ],
    "h1": [
        '''
        <h1>
        ''',
        '''
        </h1>
        '''
    ],
    "h2": [
        '''
        <h2>
        ''',
        '''
        <hr>
        </h2>
        '''
    ],
    "h3": [
        '''
        <h3>
        ''',
        '''
        <hr>
        </h3>
        '''
    ],
    "[score]": ['''<h3 id="score"> </h3> ''', ''' '''
                ],
    "p": ['''<p>''', '''</p> '''
          ],
}
