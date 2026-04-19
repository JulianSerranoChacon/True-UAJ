class ContextData:
    def __init__(self, contextStack, parentContext=None) -> None:
        self.contextStack = contextStack
        self.parentContext = parentContext

    def parseEvent(self, event) -> bool:
        pass

    def popContext(self) -> None:
        if self.contextStack:
            childContext = self.contextStack.pop()
            if self.parentContext is not None:
                self.parentContext.onPopChildContext(childContext)        
    
    def onPopChildContext(self, childContextData) -> None:
        pass

class RootContextData(ContextData):
    def __init__(self, contextStack, parentContext=None) -> None:
        super().__init__(contextStack, parentContext)
        self.games = []
    
    def parseEvent(self, event) -> bool:
        etype = event.get('type')
        if etype == "sesStart":
            from context_data import GameContextData
            game_ctx = GameContextData(self.contextStack, self)
            self.contextStack.append(game_ctx)
            return False 
        return True

    def onPopChildContext(self, childContextData) -> None:
        self.games.append(childContextData)

class GameContextData(ContextData):
    def __init__(self, contextStack, parentContext=None) -> None:
        super().__init__(contextStack, parentContext)
        self.levels = []

    def parseEvent(self, event) -> bool:
        etype = event.get('type')
        if etype == "playerCP":
            from context_data import LevelContextData
            self.contextStack.append(LevelContextData(self.contextStack, self))
            return False
        return True
    
    def onPopChildContext(self, childContextData) -> None:
        self.levels.append(childContextData)

class LevelContextData(ContextData):
    def __init__(self, contextStack, parentContext=None) -> None:
        super().__init__(contextStack, parentContext)
        self.hits = []    

    def parseEvent(self, event) -> bool:
        etype = event.get('type')
        if etype == "playerHit":
            try:
                # Limpiamos las comas de las coordenadas del nuevo JSON
                x = float(str(event['cordX']).replace(',', '.'))
                y = float(str(event['cordY']).replace(',', '.'))
                self.hits.append(dict(x=x, y=y))
            except:
                pass
        return True